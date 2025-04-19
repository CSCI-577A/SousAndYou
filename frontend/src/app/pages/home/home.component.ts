import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  searchQuery: string = '';
  userId = localStorage.getItem("user_id");
  isFirstSearch: boolean = true;
  selectedRecipe: any = null;
  showRecipeModal: boolean = false;
  chatHistory: any[] = [];
  
  constructor(private http: HttpClient) {}
  
  ngOnInit():void {
    const storedId = localStorage.getItem('user_id');
    if (!storedId) {
      this.http.get<any>('http://127.0.0.1:5000/user/create').subscribe(res => {
        localStorage.setItem('user_id', res.user_id);
        console.log('New user created:', res.user_id);
      });
    } else {
      console.log('Existing user:', storedId);
    }
  }
  
  searchItem() {
    if (!this.searchQuery.trim()) return;
    
    // Add user message to chat history
    this.chatHistory.push({
      type: 'user',
      text: this.searchQuery
    });
    
    const currentQuery = this.searchQuery;
    this.searchQuery = ''; // Clear input field immediately
    
    this.http.post<{ results: any[] }>('http://127.0.0.1:5000/search',
      { query: currentQuery, user_id: localStorage.getItem('user_id') })
      .subscribe(response => {
        console.log('Search Results:', response.results);
        
        // Set first search to false to move search bar if needed
        if (this.isFirstSearch) {
          this.isFirstSearch = false;
        }
        
        // Add each result as a system message in the chat
        if (response.results && response.results.length > 0) {
          response.results.forEach(result => {
            this.chatHistory.push({
              type: 'system',
              content: result
            });
          });
        } else {
          // Add a no-results message
          this.chatHistory.push({
            type: 'system',
            content: {
              text: "I couldn't find any recipes matching your query. Please try a different search."
            }
          });
        }
        
        // Scroll to bottom of chat
        setTimeout(() => {
          this.scrollToBottom();
        }, 100);
      });
  }
  
  scrollToBottom() {
    const chatContainer = document.querySelector('.chat-container');
    if (chatContainer) {
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  }
  
  viewRecipeDetails(content: any) {
    // Only show recipe modal if this appears to be an actual recipe
    this.selectedRecipe = content;
    this.showRecipeModal = true;
  }
  
  closeRecipeModal() {
    this.showRecipeModal = false;
    this.selectedRecipe = null;
  }
  
  parseIngredients(ingredientsText: string): string[] {
    if (!ingredientsText) return [];
    // Split by newlines and remove empty entries
    return ingredientsText.split('\n')
      .map(item => item.trim())
      .filter(item => item && !item.toLowerCase().includes('ingredients:'));
  }
  
  // Check if content appears to be a recipe
  isRecipeContent(text: string): boolean {
    if (!text) return false;
    
    // Check for common recipe indicators
    const recipeIndicators = [
      'ingredients:',
      'instructions:',
      'directions:',
      'recipe',
      'cook time',
      'prep time',
      'servings',
      'tablespoon',
      'teaspoon',
      'cup',
      'ounce',
      'pound'
    ];
    
    const lowerText = text.toLowerCase();
    return recipeIndicators.some(indicator => lowerText.includes(indicator));
  }
  
  // Handle pressing enter in the input field
  onKeyDown(event: KeyboardEvent) {
    if (event.key === 'Enter' && this.searchQuery.trim()) {
      this.searchItem();
    }
  }
  formatText(text: string): string {
    if (!text) return '';
    let formatted = text.replace(/\n/g, '<br>');
    formatted = formatted.replace(/(Steps:)/gi, '<strong>$1</strong>');
    formatted = formatted.replace(/(\d+\.\s)/g, '<br><strong>$1</strong>');
    return formatted;
  }  
}

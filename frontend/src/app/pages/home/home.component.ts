import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  searchQuery: string = '';
  userId = localStorage.getItem('user_id');
  isFirstSearch: boolean = true;
  chatHistory: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    const storedId = localStorage.getItem('user_id');
    if (!storedId) {
      this.http
        .get<any>('/${environment.apiUrl}/user/create')
        .subscribe((res) => {
          localStorage.setItem('user_id', res.user_id);
          console.log('New user created:', res.user_id);
        });
    } else {
      console.log('Existing user:', storedId);
    }
  }

  searchItem() {
    if (!this.searchQuery.trim()) return;

    const currentQuery = this.searchQuery;
    this.chatHistory.push({ type: 'user', text: currentQuery });
    this.searchQuery = '';

    this.http
      .post<{ results: any[] }>('/${environment.apiUrl}/search', {
        query: currentQuery,
        user_id: localStorage.getItem('user_id'),
      })
      .subscribe((response) => {
        console.log('Search Results:', response.results);

        if (this.isFirstSearch) {
          this.isFirstSearch = false;
        }

        if (response.results && response.results.length > 0) {
          response.results.forEach((result) => {
            this.chatHistory.push({
              type: 'system',
              content: result,
            });
          });
        } else {
          this.chatHistory.push({
            type: 'system',
            content: {
              text: "I couldn't find any recipes matching your query. Please try a different search.",
            },
          });

          const lastSystemMessage =
            response.results?.[
              response.results.length - 1
            ]?.text?.toLowerCase();
          if (lastSystemMessage && !this.isRecipeContent(lastSystemMessage)) {
            this.chatHistory.push({
              type: 'system',
              content: {
                text: 'Would you like a specific pasta recipe? For example, do you prefer tomato-based or cream-based sauces? Any ingredients you want to include or avoid?',
              },
            });
          }
        }

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

  parseIngredients(ingredientsText: string): string[] {
    if (!ingredientsText) return [];
    return ingredientsText
      .split('\n')
      .map((item) => item.trim())
      .filter((item) => item && !item.toLowerCase().includes('ingredients:'));
  }

  isRecipeContent(text: string): boolean {
    if (!text) return false;
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
      'pound',
    ];
    const lowerText = text.toLowerCase();
    return recipeIndicators.some((indicator) => lowerText.includes(indicator));
  }

  onKeyDown(event: KeyboardEvent) {
    if (event.key === 'Enter' && this.searchQuery.trim()) {
      this.searchItem();
    }
  }

  formatText(text: string): string {
    if (!text) return '';
    return text
      .replace(/(?:\r\n|\r|\n)/g, '<br>')
      .replace(/- /g, '• ')
      .replace(/\d+\./g, (match) => `<strong>${match}</strong>`)
      .replace(/([A-Z][a-z]+):/g, '<br><strong>$1:</strong>');
  }
}

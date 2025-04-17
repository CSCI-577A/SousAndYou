import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
// import { NavbarComponent } from '../../shared/navbar/navbar.component';

@Component({
  selector: 'app-home',
  standalone: true,
  // imports: [CommonModule, FormsModule, NavbarComponent],
  imports: [CommonModule, FormsModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  searchQuery: string = '';
  searchResults: string[] = [];
  userId = localStorage.getItem("user_id");
  constructor(private http: HttpClient) {}

  ngOnInit():void {
    const storedId = localStorage.getItem('user_id');
    if (!storedId) {
      this.http.get<any>('http://44.237.212.169/user/create').subscribe(res => {
        localStorage.setItem('user_id', res.user_id);
        console.log('New user created:', res.user_id);
      });
    } else {
      console.log('Existing user:', storedId);
    }}


  searchItem() {
    this.http.post<{ results: string[] }>('https://44.237.212.169/search',
      { query: this.searchQuery, user_id: localStorage.getItem('user_id') })
      .subscribe(response => {
        this.searchResults = response.results;
        console.log('Search Results:', this.searchResults);
      });
  }
}

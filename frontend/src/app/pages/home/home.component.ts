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

  constructor(private http: HttpClient) {}

  ngOnInit() {}

  searchItem() {
    this.http.post<{ results: string[] }>('http://127.0.0.1:5000/search', { query: this.searchQuery })
      .subscribe(response => {
        this.searchResults = response.results;
        console.log('Search Results:', this.searchResults);
      });
  }
}

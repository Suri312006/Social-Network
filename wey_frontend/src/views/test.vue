<template>
    <div class="summoner-search">
      <div class="search-container">
        <input
          v-model="summonerName"
          @input="handleInput"
          placeholder="Enter Summoner Name"
          class="search-input"
        />
        <button @click="searchSummoner" class="search-button">Search</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        summonerName: '',
      };
    },
    methods: {
      handleInput() {
        // You can add input validation or real-time validation here
      },
      searchSummoner() {
        // Add your summoner search logic here
        // You can make an API request to retrieve summoner data
        // and display it in your application
        console.log(`Searching for summoner: ${this.summonerName}`);
      },
    },
  };
  </script>
  
  <style scoped>
  .summoner-search {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .search-container {
    display: flex;
    align-items: center;
  }
  
  .search-input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    margin-right: 10px;
    width: 250px;
  }
  
  .search-button {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .search-button:hover {
    background-color: #0056b3;
  }
  </style>
  
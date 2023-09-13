<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
            <h3 class="mb-6 text-xl">Trends</h3>
    
            <div class="space-y-4">
                <div class="flex items-center justify-between"
                    v-for="trend in trends"
                    v-bind:key="trend.hashtag"
                >
                    <p class="text-xs">
                        <strong>#{{ trend.hashtag }}</strong><br>
                        <span class="text-gray-500">{{ trend.occurrences }} posts</span>
                    </p>
    
                    <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Explore</a>
                </div>
            </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Trends',

    data() {
        return {
            trends: []
        }
    },
    mounted(){
        this.getTrends()
    },

    methods: {
        
        getTrends(){
            axios.
                get('/api/posts/trends/')
                .then(response =>{
                    this.trends=response.data
                    console.log(response.data)
                })
                .catch(error =>{
                    console.log('error: ', error)
                })
        }
    }
    
}
</script>
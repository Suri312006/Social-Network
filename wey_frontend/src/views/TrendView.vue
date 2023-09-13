<template>

    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        
        <div class="main-center col-span-3 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg ">
                
                <h1 class ="text-xl">Trend: #{{ $route.params.id }}</h1>
            </div>
            <div 
                v-for="post in posts"
                v-bind:key="post.id" 
                class="p-4 bg-white border border-gray-200 rounded-lg">
                
                <FeedItem v-bind:post='post' />
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />

            <Trends />
        </div>
    </div>
</template>

<script>
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import axios from 'axios'

export default {
    name: 'FeedView',
    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },

    data(){
        return{
            posts: [],

        }
    },



    mounted() {
        this.getFeed()
    },
    watch: {
        '$route.params.id': {
            handler:function() {
                this.getFeed()
            },
        deep: true,
        immediate: true
        },
        
    },
    methods: {
        getFeed() {
            axios
                .get(`/api/posts/?trend=${this.$route.params.id}`)
                .then(response => {
                    
                    this.posts = response.data

                })
                .catch(error => {
                    console.log('error', error)
                })
        },


    }
}
</script>
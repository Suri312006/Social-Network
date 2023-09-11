<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        
        <div class="main-center col-span-3 space-y-4">
            
            <!--div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>

                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>-->

            <div 
                v-if="post.id"
                class="p-4 bg-white border border-gray-200 rounded-lg">
                
                <FeedItem v-bind:post='post' />
            </div>

            <div class=" p-4 ml-6  bg-white border border-gray-200 rounded-lg"
                v-for="comment in post.comments"
                v-bind:key="comment.id">
                
                <CommentItem v-bind:comment="comment"/>
            </div>

            <div class="ml-6 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you think?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100">
        
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">comment</button>
                    </div>
                </form>
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
import CommentItem from '../components/CommentItem.vue'
import axios from 'axios'


export default {
    name: 'PostView',
    components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem,
    CommentItem,
    CommentItem
},

    data(){
        return{
            post: {
                id: null,
                comments: []
                
            },
            body: '',

        }
    },



    mounted() {
        this.getPost()
    },
    methods: {
        getPost() {
            axios
                .get(`/api/posts/${this.$route.params.id}/`)
                .then(response => {
                    this.post = response.data.post
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post(`/api/posts/${this.$route.params.id}/comment/`,{
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)
                    this.post.comments.push(response.data.comment)
                    this.post.comments_count +=1
                    this.body=''
                
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>
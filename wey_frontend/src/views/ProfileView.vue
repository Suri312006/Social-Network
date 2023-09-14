<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full">

                <p><strong>{{ user.name}}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{name: 'friends', params: {id: user.id}}" class="text-xs text-gray-500">{{ user.friends_count }} friends</RouterLink>
                    <p class="text-xs text-gray-500">{{user.posts_count}} posts</p>
                </div>

                <div class ="mt-6">
                    <button  v-if="userStore.user.id !== user.id" class="inline-block py-2 px-4 bg-purple-600 text-white rounded-lg" @click="sendFriendshipRequest">
                        Add as Friend
                    </button>

                    <button  v-if="userStore.user.id !== user.id" class="inline-block mt-3 py-2 px-4 bg-purple-600 text-white rounded-lg" @click="sendDirectMessage">
                        Start Conversation
                    </button>

                </div>
                
                <div v-if="userStore.user.id === user.id" class ="mt-6">

                    <RouterLink to="/edit-profile" class="inline-block py-2 px-4 mr-2 bg-purple-600 text-white rounded-lg">
                        Edit Profile
                    </RouterLink>

                    <button class="inline-block py-2 px-4 bg-red-600 text-white rounded-lg" @click="logout">
                        Logout
                    </button>

                    
                </div>
                
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
                >
                
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>

                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <div v-for="post in posts"
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
import axios from 'axios'
import FeedItem from '../components/FeedItem.vue'
import {useUserStore} from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import { RouterLink } from 'vue-router'

export default (await import ('vue')).defineComponent({
    name: 'ProfileView',
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },


    components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem,
    RouterLink
},

    data(){
        return{
            posts: [],
            user: {
                id: null
            },

            body: '',

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

        'user.friends_count':{
            handler(newValue, oldValue) {
                if (newValue === oldValue +1){
                    this.newFriendToast()
                }
            },
        immediate:true
        }
        

        
        

    },

    methods: {
        sendDirectMessage(){
            console.log('send direct message')
            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response =>{
                    console.log(response.data)

                    this.$router.push('/chat')
                })
                .catch(error =>{
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    
                    this.posts = response.data.posts
                    this.user = response.data.user
                    
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post('/api/posts/create/',{
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)
                    this.posts.unshift(response.data)
                    this.body=''
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    if(response.data.message == 'created'){
                        this.toastStore.showToast(5000, 'Friend Request Sent!', 'bg-emerald-500')
                    }

                    if(response.data.message =='already exists'){
                        this.toastStore.showToast(5000, 'Request Already Exists', 'bg-red-300')
                    }

                })
                .catch(error => {
                    
                    console.log('error', error)
                })
        },

        newFriendToast(){

            this.toastStore.showToast(5000, 'New Friend Added!', 'bg-emerald-500')

        },
        
        logout() {
            console.log('logout')
            this.userStore.removeToken()

            this.$router.push('/login')

        }

    }
})
</script>
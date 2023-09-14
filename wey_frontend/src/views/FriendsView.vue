<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full">

                <p><strong>{{ user.name}}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">{{user.friends_count}} friends</p>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
            v-if="friendshipRequests.length>0"
            class="p-4 bg-white border border-gray-200 rounded-lg centered gap-4">

            <h2 class="text-xl mb-3">Friendship Requests</h2>
                <div 
                v-for="friendshipRequest in friendshipRequests"
                v-bind:key="friendshipRequest.created_by.id"
                 class="p-4 text-center bg-gray-100 rounded-lg">
                    <img :src="friendshipRequest.created_by.get_avatar" class="mx-auto rounded-full ">

                    <p>
                        <strong>
                            <RouterLink :to="{'name': 'profile', params:{'id': friendshipRequest.created_by.id}}">{{ friendshipRequest.created_by.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{ friendshipRequest.created_by.friends_count  }} friends</p>
                        <p class="text-xs text-gray-500">{{user.posts_count}} posts</p>
                    </div>

                    <div class="mt-6 space-x-4 ">
                        <button class="inline-block py-2 px-4 bg-purple-600 text-white rounded-lg" @click="handleRequest('accepted', friendshipRequest.created_by.id)">
                            Accept 
                        </button>
                        <button class="inline-block py-2 px-4 bg-red-600 text-white rounded-lg" @click="handleRequest('rejected', friendshipRequest.created_by.id)">
                            Deny 
                        </button>
                    </div>
                </div>
                <hr>
            </div>

            
            <div 
            v-if="friends.length>0"
            class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4">

            
                <div 
                v-for="friend in friends"
                v-bind:key="friend.id"
                 class="p-4 text-center bg-gray-100 rounded-lg">
                    <img :src="friend.get_avatar" class="mb-6 mx-auto rounded-full">

                    <p>
                        <strong>
                            <RouterLink :to="{'name': 'profile', params:{'id': friend.id}}">{{ friend.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{friend.friends_count}} friends</p>
                        <p class="text-xs text-gray-500">{{user.posts_count}} posts</p>
                    </div>
                </div>

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


export default {
    name: 'FriendsView',
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },


    components: {
        PeopleYouMayKnow,
        Trends,
    },

    data(){
        return{

            user:{},
            friendshipRequests: [],
            friends: []

        }
    },



    mounted() {
        this.getFriends()
    },


    methods: {
        getFriends() {
            axios
                .get(`/api/friends/${this.$route.params.id}/`)
                .then(response => {
                    this.friendshipRequests = response.data.requests
                    this.friends = response.data.friends
                    this.user = response.data.user
                    
                    console.log('data', response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        handleRequest(status, friendship_request_id) {
            console.log('handle request', status)

            axios
                .post(`/api/friends/${friendship_request_id}/${status}/`)
                .then(response => {

                    if(response.message == 'request accepted'){
                        this.toastStore.showToast(5000, 'Friend Request Accepted!', 'bg-emerald-500')


                    }

                    console.log(response.data)
                })
                .catch(error =>{
                    console.log('error', error)
                })
        }


    }
}
</script>
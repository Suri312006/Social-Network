<template>
    chat
</template>

<script>
export default{
    name: 'chat',

    mounted(){
        this.getConversations()
    },

    methods: {
        getConversations(){
            console.log('getConversations')
        }
    }
}
</script>
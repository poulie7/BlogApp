<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const article = ref([]); // Initialize as null since we're looking for a single article
const articles = ref([]);
const route = useRoute();
const articleId = parseInt(route.params.id);


const getPosts = async () => {
    try {
        const response = await axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api',
        });
        return response.data; 
    } catch (error) {
        console.error('Error fetching articles:', error);
        return [];
    }
};


const findArticleById = (id) => {
    return articles.value.find(article => article.id === id);
};


onMounted(async () => {
    try {
        const fetchedArticles = await getPosts();
        articles.value = fetchedArticles; 

        // Find the article with the matching ID
        article.value = findArticleById(articleId);

    } catch (error) {
        console.error('Error in onMounted:', error);
    }
});

</script>

<template>
    <main>
        <h1>{{ article.article_header }}</h1>
        <div class="text">
            <p>{{article.article}}</p>
        </div>
        
    </main>
</template>

<style scoped>
h1{
    text-align: center;
    margin: 2em;
    text-transform: uppercase;
}
.text { 
    margin: 1em;
    text-indent: 50px;
    text-align: justify;
    border: 1px solid gray;
    padding: 8px;
}
</style>
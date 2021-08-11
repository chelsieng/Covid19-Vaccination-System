import {createRouter, createWebHistory} from 'vue-router'
import Query from '../components/Query.vue';
import Create from '../components/Create.vue';
import Modify from '../components/Modify.vue';

const routes = [
    {
        path: '/create',
        name: 'Create',
        component: Create
    },
    {
        path: '/query',
        name: 'Query',
        component: Query
    },
    {
        path: '/edit/:table',
        name: 'Modify',
        component: Modify,
        props: true
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

<template>
    <v-layout>
        <v-app-bar color="primary" height="48">
            <v-app-bar-title class="text-h6 ms-3">
                Clinic Care
            </v-app-bar-title>
            <template v-slot:prepend>
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            </template>
        </v-app-bar>

        <v-navigation-drawer v-model="drawer">
            <v-list-item v-for="link, index in naviLinks" :to="link.path">{{ link.title }}</v-list-item>
        </v-navigation-drawer>

        <v-main>
            <v-container>
                <NuxtPage />
            </v-container>
        </v-main>
    </v-layout>
</template>

<script setup>

const drawer = ref(false)

const naviLinks = [
    {
        title: 'Home',
        path: '/'
    }, 
    {
        title: 'Consultation Notes',
        path: '/consultations'
    },
    {
        title: 'Diagnoses',
        path: '/diagnoses'
    }
]
</script>
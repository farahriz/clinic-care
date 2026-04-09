<template>
    <h1>Consultations</h1>
    <v-btn color="primary"  text="Add new consulation" prepend-icon="mdi-plus">
    </v-btn>

    <ConsultationForm></ConsultationForm>

    <v-data-table class="mt-5"></v-data-table>
</template>

<script setup lang="ts">
import ConsultationForm from '~/components/consultationForm.vue';

const consulations = ref([])
</script>
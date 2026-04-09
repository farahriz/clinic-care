<template>
    <v-form>
        <v-text-field label="Patient" v-model="formData.patient"></v-text-field>
        <v-text-field label="Consultation Date" v-model="formData.consultDate"></v-text-field>
        <v-autocomplete label="Diagnosis" v-model="formData.code"></v-autocomplete>
        <v-textarea label="Description" v-model="formData.description"></v-textarea>
    </v-form>
</template>

<script setup lang="ts">
const formData = ref({
    id: null,
    code: "",
    patient: "",
    consultDate: "",
    description: ""
})
</script>
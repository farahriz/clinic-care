<template>
    <v-card title="List of Diagnosis Codes">
        <template v-slot:text>
            <v-text-field
                v-model="search"
                label="Search"
                prepend-inner-icon="mdi-magnify"
                variant="outlined"
                hide-details
                single-line
            ></v-text-field>
        </template>
        <v-data-table :items="diagnoses"  :search="search"/>
    </v-card>
</template>

<script setup>
const diagnoses = await useFetchDiagnosis()
const search = ref("")
</script>
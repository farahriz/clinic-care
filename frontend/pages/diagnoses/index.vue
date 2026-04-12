<template>
    <h1>List of Diagnosis Codes</h1>
    {{ diagnoses }}
</template>

<script setup>
const diagnoses = await useFetchDiagnosis()



</script>
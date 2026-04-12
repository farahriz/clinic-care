<template>
    <h1>Consultations</h1>
        <v-btn color="primary"  text="Add new consulation" prepend-icon="mdi-plus" :to="{name: 'consultations-add'}">
        </v-btn>

    <v-data-table class="mt-5" 
      :items="consulations" 
      :headers="headers">
    </v-data-table>
</template>

<script setup>
const headers = [
    {title: "ID", value: "id"},
    {title: "Patient", value: "patient", key: "patient"},
    {title: "Code", key: "diagnosis_id", value: item => getDiagnosisCode(item.diagnosis_id)},
    {title: "Description", value: "desc"},
    {title: "Created at", value: item => new Date(item.created_at).toUTCString(), key: "created_at"}
]
const consulations = ref(await useGetAllConsultationNotes())
const diagnoses = ref(await useFetchDiagnosis())

function getDiagnosisCode(id){
    const code = diagnoses.value.find(code => code.id == id)
    return code.code
}

</script>
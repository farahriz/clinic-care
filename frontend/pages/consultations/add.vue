<template>
    <h1>Add new consulation note</h1>
    <v-btn prepend-icon="mdi-content-save" color="primary" text="Save changes" class="mb-5" @click="saveChanges"></v-btn>
    <ConsultationForm :readonly="false" v-model:consultNoteData="consultNoteData"/>
    <v-snackbar v-model="snackbar" :color="hasError ? 'red-lighten-3' : 'green-lighten-3'">
        {{ snackbarMessage }}
    </v-snackbar>
</template>

<script setup>
const snackbar = ref(false)
const snackbarMessage = ref(null)
const hasError = ref(false)

const consultNoteData = ref({
    patient: "",
    code: "",
    desc: ""
})

async function saveChanges(){
    snackbar.value = false
    const { data, status, error } = await useCreateConsulationNote(consultNoteData.value)
    console.log(status.value)
    if(status.value == 'success'){
        hasError.value = false
        snackbarMessage.value = "Success, redirecting to table"
        snackbar.value = true
        navigateTo({name: 'consultations'})
    }
    if(error){
        console.log('oops there is an error')
        console.error(error.value.data)
        hasError.value = true
        snackbarMessage.value = error.value.data.detail
        snackbar.value = true
    }
}

</script>
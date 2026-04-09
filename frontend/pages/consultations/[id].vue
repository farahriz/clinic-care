<template>
    <h1>Consulation Data</h1>
    <v-row>
        <v-btn prepend-icon="mdi-pencil" color="secondary" text="Edit" class="mb-5" @click="initEditMode"></v-btn>
        <v-spacer />
        <v-btn prepend-icon="mdi-content-save" color="primary" text="Save changes" class="mb-5" @click="saveChanges" v-if="!readOnly"></v-btn>
    </v-row>
    <v-alert type="warning" variant="tonal" v-if="hasUnsavedChanges" >
        You have unsaved changes
    </v-alert>
    <v-text-field label="ID" disabled v-model="consultNoteData.id"></v-text-field>
    <ConsultationForm :readOnly="readOnly" v-model:consultNoteData="consultNoteData">
    </ConsultationForm>
</template>

<script setup lang="ts">
import ConsultationForm from '~/components/consultationForm.vue';

const readOnly = ref(true)
const hasUnsavedChanges = ref(false)

const consultNoteData = ref({
    id: "",
    patient: "",
    consultDate: "",
    code: "",
    description: ""
})

function initEditMode(){
    readOnly.value = !readOnly.value
}

function saveChanges(){
    hasUnsavedChanges.value = false
}

</script>
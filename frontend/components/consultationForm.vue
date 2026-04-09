<template>
    <v-form>
        <v-text-field :disabled="readOnly" label="Patient" v-model="formData.patient"></v-text-field>
        <v-text-field  :disabled="readOnly" label="Consultation Date" v-model="formData.consultDate"></v-text-field>
        <v-autocomplete :disabled="readOnly" label="Diagnosis" v-model="formData.code"></v-autocomplete>
        <v-textarea :disabled="readOnly" label="Description" v-model="formData.description"></v-textarea>
    </v-form>
</template>

<script setup lang="ts">
const formData = defineModel('consultNoteData')

const props = defineProps({
    readOnly: {
        type: Boolean,
        default: false
    }
})

// const formData = ref({
//     id: null,
//     code: "",
//     patient: "",
//     consultDate: "",
//     description: ""
// })
</script>
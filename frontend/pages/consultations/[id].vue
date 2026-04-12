<template>
    <h1>Consulation Data</h1>
    <v-row>
        <v-btn prepend-icon="mdi-pencil" color="secondary" text="Edit" class="mb-5" @click="initEditMode"></v-btn>
        <v-spacer />
        <v-tooltip text="Feature coming soon...">
            <template v-slot:activator="{props}">
                <v-btn v-bind="props" 
                    prepend-icon="mdi-content-save" color="primary" text="Save changes" class="mb-5" @click="saveChanges" v-if="!readOnly"></v-btn>
            </template>
        </v-tooltip>
    </v-row>
    <v-alert type="warning" variant="tonal" v-if="hasUnsavedChanges" >
        You have unsaved changes
    </v-alert>
    <v-text-field label="ID" disabled v-model="consultNoteData.id"></v-text-field>
    <ConsultationForm :readOnly="readOnly" v-model:consultNoteData="consultNoteData">
    </ConsultationForm>
</template>

<script setup>
import ConsultationForm from '~/components/consultationForm.vue';

const route = useRoute()

const readOnly = ref(true)
const hasUnsavedChanges = ref(false)
const consultNoteData = ref({
    id: route.params.id,
    patient: "",
    diagnosis_id: null,
    desc: ""
})
const fetchedData = await useGetConsulationNoteById(route.params.id)

consultNoteData.value.patient = fetchedData.patient
consultNoteData.value.diagnosis_id = fetchedData.diagnosis_id
consultNoteData.value.desc = fetchedData.desc

watch(
    () => consultNoteData,
    (newVal, oldVal) => {
        Object.keys(newVal).forEach(key => {
            if(fetchedData[key] != newVal[key]){
                hasUnsavedChanges.value = true
                return
            }
        })
    },
    {deep: true}
)

function initEditMode(){
    readOnly.value = !readOnly.value
}

function saveChanges(){
    hasUnsavedChanges.value = false
}

</script>
<template>
    <v-form>
        <v-text-field :disabled="readOnly" label="Patient" v-model="formData.patient"></v-text-field>
        <v-autocomplete 
            :disabled="readOnly" label="Diagnosis" 
            clearable
            chips
            :filter-keys="['name', 'code']"
            :items="diagnoses"
            item-title="code" 
            item-value="id"
            v-model="formData.diagnosis_id">
            <template v-slot:chip="{props, item}">
                <v-chip v-bind="props" :text="`${item.code} - ${item.name}`"></v-chip>
            </template>
            <template v-slot:item="{props, item}">
                <v-list-item v-bind="props"
                    :title="item.code"
                    :subtitle="item.name"
                >
                </v-list-item>
            </template>
        </v-autocomplete>
        <v-textarea :disabled="readOnly" label="Description" v-model="formData.desc"></v-textarea>
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

const diagnoses = ref(await useFetchDiagnosis())
</script>
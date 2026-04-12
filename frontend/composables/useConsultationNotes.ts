interface ConsultNote {
    id?: string,
    diagnosisId: string,
    desc: string
    patient: string,
    created_at: string,
}

interface CreateConsult {
    diagnosis_id: string,
    description: string
    patient?: string,
    consultDate?: string
}

export async function useGetAllConsultationNotes() {
    const apiUrl = `/api/consultation`
    const resp = await $fetch(apiUrl, {
        method: 'GET'
    })
    let notes = resp as ConsultNote[]
    return notes
}

export async function useGetConsulationNoteById(consultId: string) {
    const apiUrl = `/api/consultation/${consultId}`
    const resp = await $fetch(apiUrl, {
        method: 'GET'
    })
    return resp as ConsultNote
}

export async function useCreateConsulationNote(consulationNote: CreateConsult){
    const apiUrl = `/api/consultation`
    const resp = await useFetch(apiUrl, {
        method: 'POST',
        body: consulationNote
    })
    return resp
}

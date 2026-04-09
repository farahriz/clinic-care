interface ConsultNote {
    id?: string,
    code: string,
    description: string
    patient?: string,
    consultDate?: string
    createdAt: string,
    createdBy: string,
    updatedAt: string,
    updatedBy: string
}

interface CreateConsult {
    code: string,
    description: string
    patient?: string,
    consultDate?: string
}

interface EditConsult {
    id: string,
    code: string,
    description: string
    patient?: string,
    consultDate?: string
}

export async function getAllConsultationNotes() {
    let notes: ConsultNote[] = []
    return notes
}

export async function useGetConsulationNoteById(consultId: string) {
    let note: ConsultNote[] | null = null
    return note
}

export async function useCreateConsulationNote(consulationNote: CreateConsult){
    return
}

export async function useUpdateConsulationNote(consulationNote: EditConsult){
    return
}

export async function useDeleteConsultaionNote(consultId: string){
    return
}

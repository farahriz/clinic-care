interface Diagnosis {
    id: string,
    code: string,
    name: string
}

export async function useFetchDiagnosis(offset= 0, limit = 200, search?: string | null){
    const path = 'diagnosis'
    let apiUrl = `/api/${path}?offset=${offset}&limit=${limit}`
    if(search){
        apiUrl+=`&search=${search}`
    }

    const resp = await $fetch(apiUrl, {
        method: 'GET'
    })
    return resp
}
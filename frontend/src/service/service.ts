import { httpClient } from '../http/http'
import { ElNotification } from 'element-plus'
import type { SystemStatus } from '../type'
// 获取可用数据集
export async function listDataset():Promise<Array<string>>{
    const endpoint:string = 'list_dataset'
    const res = await httpClient.post(endpoint)
    if(res.data.datasets.length === 0){
        ElNotification({
            title: '提示',
            message: '请检查可用数据集',
            type: 'warning',
        })
    }
    return res.data.datasets
}
export async function loadDataSet(data:any):Promise<string>{
    const endpoint = 'load_dataset'
    const res = await httpClient.post(endpoint,{body:JSON.stringify(data)})
    return res.data.status as string
}
export async function startSut():Promise<SystemStatus>{
    const endpoint = 'start_sut'
    const res = await httpClient.post(endpoint)
    return res.data
}
export async function startTest(data:any){
    const endpoint = 'start_test'
    const res:any = await httpClient.post(endpoint,{body:JSON.stringify(data)})
    return res.data
}
export async function progress(uuid:string){
    const endpoint = 'progress'
    const res:any = await httpClient.post(endpoint,{body:JSON.stringify({'uuid':uuid})})
    return res.data
}
export async function result(uuid:string){
    const endpoint = 'result'
    const res:any = await httpClient.post(endpoint,{body:JSON.stringify({'uuid':uuid})})
    return res.data
}
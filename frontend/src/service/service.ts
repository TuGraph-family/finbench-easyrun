import {httpClient} from '../http/http'
import {ElNotification} from 'element-plus'
import type {ProgressResult, SystemStatus} from '../type'
// 获取可用数据集
export async function listDataset():Promise<Array<string>>{
    let endpoint:string = 'list_dataset'
    let res = await httpClient.post(endpoint)
    if(res.data.datasets.length === 0){
        ElNotification({
            title: '提示',
            message: '请检查可用数据集',
            type: 'warning',
        })
    }
    return res.data.datasets
}

// 加载数据集
export async function loadDataSet():Promise<string>{
    let endpoint = 'load_dataset'
    let res = await httpClient.post(endpoint)
    return res.data.status as string
}


// 启动系统
export async function startSut():Promise<SystemStatus>{
    let endpoint = 'start_sut'
    let res = await httpClient.post(endpoint)
    return res.data
}
// 开始测试并获取进度
export async function progress(uuid:string){
    let endpoint = 'progress'
    let res:any = await httpClient.post(endpoint,{body:JSON.stringify({'uuid':uuid})})
    return res.data
}
// 获取测试结果
export async function result(uuid:string){
    let endpoint = 'result'
    let res:any = await httpClient.post(endpoint,{body:JSON.stringify({'uuid':uuid})})
    return res.data
}
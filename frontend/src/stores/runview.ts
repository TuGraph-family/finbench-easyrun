import { defineStore } from 'pinia'
import type { SystemInfo, DataInfo, ModeInfo,DataList,ProgressResult,SystemStatus,FinResult } from '../type'
import {listDataset,loadDataSet,startSut,progress,result} from '../service/service'
interface State {
  systemInfo: SystemInfo;
  dataLoad:Boolean,
  dataInfo: DataInfo,
  modeInfo: ModeInfo,
  dataList: DataList;
  progressResult:ProgressResult,
  systemStatus:SystemStatus,
  result:FinResult
}

export const useRunviewStore = defineStore('runview', {
  state: (): State => {
    // 尝试从 localStorage 中读取 systemInfo 数据
    let storedSystemInfo = localStorage.getItem('graphbench_systemInfo');
    let initialSystemInfo: SystemInfo = storedSystemInfo ? JSON.parse(storedSystemInfo) : {
      model: '',
      os: '',
      cpu: '',
      memory: '',
      storage: '',
      network: ''
    };
    let storedDataInfo = localStorage.getItem('graphbench_dataInfo');
    let initialDataInfo: DataInfo = storedDataInfo ? JSON.parse(storedDataInfo) : {
      data:''
    };
    let storedModeInfo = localStorage.getItem('graphbench_modeInfo')
    let initialModeInfo: ModeInfo = storedModeInfo ? JSON.parse(storedModeInfo) : {
      mode:'validate'
    };
    let sotreProgressResult = localStorage.getItem('graphbench_progressResult')
    let initialProgressResult: ProgressResult = sotreProgressResult?JSON.parse(sotreProgressResult) : {
      uuid:'',
      status:'stop'
    };
    let sotreSystemStatus = localStorage.getItem('graphbench_systemStatus')
    let initialSystemStatus: SystemStatus = sotreSystemStatus?JSON.parse(sotreSystemStatus) : {
      uuid:'',
      status:'stop'
    };
    let result:any
    if(initialProgressResult.status === 'finished'){
      debugger
      result =JSON.parse(localStorage.getItem('graphbench_result') as string) 
    }else{
      result = null
    }
    return {
      systemInfo: initialSystemInfo,
      dataLoad:localStorage.graphbench_dataLoad === 'true'||false,
      dataInfo: initialDataInfo,
      modeInfo: initialModeInfo,
      progressResult:initialProgressResult,
      systemStatus:initialSystemStatus,
      dataList: [],
      result:result
    }
  },
  actions: {
    async getListDataset(){
      let res = await listDataset()
      this.dataList = res
    },
    async runLoadDatase():Promise<string>{
      let res = await loadDataSet()
      return res
    },
    async startSut():Promise<SystemStatus>{
      let res = await startSut()
      return res
    },
    async getProgress(uuid:string):Promise<ProgressResult>{
      let res = await progress(uuid)
      return res

    },
    async getResult(uuid:string):Promise<FinResult>{
      let res = await result(uuid)
      return res
    },
    updateDataInfo(newDataInfo: { data: string }) {
      this.dataInfo = newDataInfo;
      localStorage.setItem('graphbench_dataInfo', JSON.stringify(newDataInfo));
    },
    updateSystemInfo(newSystemInfo: SystemInfo) {
      this.systemInfo = newSystemInfo;
      localStorage.setItem('graphbench_systemInfo', JSON.stringify(newSystemInfo));
    },
    updateLoadData(newDataLoad:boolean){
      this.dataLoad = newDataLoad
      localStorage.setItem('graphbench_dataLoad',JSON.stringify(newDataLoad))
    },
    updateModeInfo(newModeInfo:ModeInfo){
      this.modeInfo = newModeInfo
      localStorage.setItem('graphbench_modeInfo',JSON.stringify(newModeInfo))
    },
    updateSystemStatus(newSystemStatus:SystemStatus){
      this.systemStatus = newSystemStatus
      localStorage.setItem('graphbench_systemStatus',JSON.stringify(newSystemStatus))
    },
    updateProgressResult(newProgressResult:ProgressResult){
      this.progressResult = newProgressResult
      localStorage.setItem('graphbench_progressResult',JSON.stringify(newProgressResult))
    },
    updateResult(newResult:FinResult){
      this.result = newResult
      localStorage.setItem('graphbench_result',JSON.stringify(newResult))
    }
  }
});

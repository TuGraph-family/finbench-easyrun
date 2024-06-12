import { defineStore } from 'pinia'
import type { SystemInfo, DataInfo, ModeInfo, DataList, ProgressResult, SystemStatus, FinResult } from '../type'
import { listDataset, startSut, progress, result, startTest, resetAll } from '../service/service'
interface State {
  systemInfo: SystemInfo;
  dataInfo: DataInfo,
  modeInfo: ModeInfo,
  dataList: DataList;
  progressResult: ProgressResult,
  systemStatus: SystemStatus,
  result: FinResult
  isReseting: boolean
}

export const useRunviewStore = defineStore('runview', {
  state: (): State => {
    // 尝试从 localStorage 中读取 systemInfo 数据
    const storedSystemInfo = localStorage.getItem('graphbench_systemInfo');
    const initialSystemInfo: SystemInfo = storedSystemInfo ? JSON.parse(storedSystemInfo) : {
      model: '',
      os: 'UOS Server 20',
      cpu: 'Phytium FTC662 64c',
      memory: '256GiB',
      storage: '',
      network: ''
    };
    const storedDataInfo = localStorage.getItem('graphbench_dataInfo');
    const initialDataInfo: DataInfo = storedDataInfo ? JSON.parse(storedDataInfo) : {
      data: ''
    };
    const storedModeInfo = localStorage.getItem('graphbench_modeInfo')
    const initialModeInfo: ModeInfo = storedModeInfo ? JSON.parse(storedModeInfo) : {
      mode: 'validate'
    };
    const sotreProgressResult = localStorage.getItem('graphbench_progressResult')
    const initialProgressResult: ProgressResult = sotreProgressResult ? JSON.parse(sotreProgressResult) : {
      status: '',
      duration: 0,
      progress: 0,
      num_lines: 0,
      phase: '',
      logs: []
    };
    const sotreSystemStatus = localStorage.getItem('graphbench_systemStatus')
    const initialSystemStatus: SystemStatus = sotreSystemStatus ? JSON.parse(sotreSystemStatus) : {
      uuid: ''
    };
    let result: any
    if (initialProgressResult.status === 'completed') {
      result = JSON.parse(localStorage.getItem('graphbench_result') as string)
    } else {
      result = null
    }
    return {
      systemInfo: initialSystemInfo,
      dataInfo: initialDataInfo,
      modeInfo: initialModeInfo,
      progressResult: initialProgressResult,
      systemStatus: initialSystemStatus,
      dataList: [],
      result: result,
      isReseting: false
    }
  },
  actions: {
    async getListDataset() {
      const res = await listDataset()
      this.dataList = res
    },
    async startSut(): Promise<SystemStatus> {
      const res = await startSut()
      return res
    },
    async getProgress(uuid: string): Promise<ProgressResult> {
      const res = await progress(uuid)
      return res

    },
    async getResult(uuid: string): Promise<FinResult> {
      const res = await result(uuid)
      return res
    },
    async startTest(data: any): Promise<any> {
      const res = startTest(data)
      return res
    },
    async resetAll(): Promise<any> {
      const res = resetAll()
      this.updateDataInfo({ data: '' })
      this.updateModeInfo({ mode: 'validate' })
      this.updateSystemInfo({
        model: '',
        os: '',
        cpu: '',
        memory: '',
        storage: '',
        network: ''
      })
      this.updateSystemStatus({ uuid: '' })
      this.updateProgressResult({
        status: '',
        duration: 0,
        progress: 0,
        num_lines: 0,
        phase: '',
        logs: []
      })
      this.updateResult({
        "duration": 0,
        "warmup": 0,
        "ops": 0,
        "query_on_time": 0,
        "throughput": 0,
        "detail": []
      })
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
    updateModeInfo(newModeInfo: ModeInfo) {
      this.modeInfo = newModeInfo
      localStorage.setItem('graphbench_modeInfo', JSON.stringify(newModeInfo))
    },
    updateSystemStatus(newSystemStatus: SystemStatus) {
      this.systemStatus = newSystemStatus
      localStorage.setItem('graphbench_systemStatus', JSON.stringify(newSystemStatus))
    },
    updateProgressResult(newProgressResult: ProgressResult) {
      let n = newProgressResult.num_lines - this.progressResult.num_lines
      let logs: any[] = []
      if (newProgressResult.num_lines > 0) {
        logs = [...this.progressResult.logs, ...newProgressResult.logs.slice(-n)]
      } else {
        logs = [...this.progressResult.logs]
      }
      newProgressResult.logs = logs
      this.progressResult = newProgressResult
      localStorage.setItem('graphbench_progressResult', JSON.stringify(newProgressResult))
    },
    updateResult(newResult: FinResult) {
      this.result = newResult
      localStorage.setItem('graphbench_result', JSON.stringify(newResult))
    },
    updateIsReseting(status: boolean) {
      this.isReseting = status
    }
  }
});

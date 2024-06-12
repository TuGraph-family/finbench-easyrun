import { defineStore } from 'pinia'
import type { SystemInfo, DataInfo, ModeInfo, DataList, ProgressResult, SystemStatus, FinResult } from '../type'
import { listDataset, startSut, progress, result, startTest } from '../service/service'
interface State {
  systemInfo: SystemInfo;
  dataInfo: DataInfo,
  modeInfo: ModeInfo,
  dataList: DataList;
  progressResult: ProgressResult,
  systemStatus: SystemStatus,
  result: FinResult
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
      uuid: '',
      status: 'stop',
      logs: {}
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
      result: result
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
    async getTestProgress(uuid: string, startTime: number): Promise<ProgressResult> {
      const DEFAULT_DURATION = 20;
      const data: ProgressResult = {
        status: 'in_progress',
        duration: 0,
        progress: 0,
        logs: {}
      };
      function generateRandomLog(progress: number): string {
        const logs = [
          `INFO: System check completed. Progress: ${progress.toFixed(2)}%`,
          `WARNING: Disk usage is high. Progress: ${progress.toFixed(2)}%`,
          `ERROR: Network latency detected. Progress: ${progress.toFixed(2)}%`,
          `DEBUG: Memory allocation successful. Progress: ${progress.toFixed(2)}%`,
          `TRACE: Entering phase ${progress.toFixed(2)}. Progress: ${progress.toFixed(2)}%`
        ];
        return logs[Math.floor(Math.random() * logs.length)];
      }
      return new Promise<ProgressResult>((resolve) => {
        const elapsedTime = (Date.now() - startTime) / 1000;
        const progress = Math.min((elapsedTime / DEFAULT_DURATION) * 100, 100);
        data.duration = parseFloat(elapsedTime.toFixed(2));
        data.progress = parseFloat(progress.toFixed(2));
        const randomLog = generateRandomLog(progress);
        const logTime = new Date().toISOString();
        data.logs[logTime] = randomLog;
        if (progress >= 100) {
          data.status = 'completed';
        }
        resolve(data)
      });
    },
    async getTestResult(uuid: string): Promise<FinResult> {
      console.log('uuid:', uuid)
      const data = await import('@/mock/result-mock.json');
      return data
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
    updateProgressResult(newProgressResult: ProgressResult, isInit?: boolean) {
      let logs = { ...this.progressResult.logs, ...newProgressResult.logs }
      if (isInit) {
        logs = {}
      }
      newProgressResult.logs = logs
      this.progressResult = newProgressResult
      localStorage.setItem('graphbench_progressResult', JSON.stringify(newProgressResult))
    },
    updateResult(newResult: FinResult) {
      this.result = newResult
      localStorage.setItem('graphbench_result', JSON.stringify(newResult))
    }
  }
});

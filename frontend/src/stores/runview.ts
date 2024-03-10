import { defineStore } from 'pinia'
import type { SystemInfo, DataInfo, ModeInfo } from '../type'

interface State {
  systemInfo: SystemInfo;
  dataInfo: DataInfo,
  modeInfo: ModeInfo,
  dataList: Array<string>;
}

export const useRunviewStore = defineStore('runview', {
  state: (): State => {
    // 尝试从 localStorage 中读取 systemInfo 数据
    const storedSystemInfo = localStorage.getItem('graphbench_systemInfo');
    const initialSystemInfo: SystemInfo = storedSystemInfo ? JSON.parse(storedSystemInfo) : {
      model: '',
      os: '',
      cpu: '',
      memory: '',
      storage: '',
      network: ''
    };

    return {
      systemInfo: initialSystemInfo,
      dataInfo: {
        data: ''
      },
      modeInfo: {
        mode: 'validate'
      },
      dataList: []
    }
  },
  actions: {
    updateSystemInfo(newSystemInfo: SystemInfo) {
      this.systemInfo = newSystemInfo;
      // 将新的 systemInfo 保存到 localStorage
      localStorage.setItem('graphbench_systemInfo', JSON.stringify(newSystemInfo));
    }
  }
});

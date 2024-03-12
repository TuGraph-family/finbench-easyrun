

// 系统配置
export interface SystemInfo {
    model: string;
    os: string;
    cpu: string;
    memory: string;
    storage: string;
    network: string;
}

// 数据配置
export interface DataInfo {
    data: string
}

// 模式配置
// 专门为 benchmark 模式定义的接口
interface BenchmarkInfo {
    tcr: number;
    ops: number;
    mode: 'benchmark';
}

// validate 模式没有 tcr 和 ops
interface ValidateInfo {
    mode: 'validate';
}

export type ModeInfo = BenchmarkInfo | ValidateInfo;

// 数据列表
export  type DataList = Array<string>
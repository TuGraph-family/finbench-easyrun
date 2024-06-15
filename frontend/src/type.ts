

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
export type DataList = Array<string>


// 进度结果

export type ProgressResult = {
    "status": string,
    "duration": number,
    "progress": number,
    "num_lines": number,
    "phase": string,
    "runtime": number,
    "operations": number,
    "throughput": number,
    "logs": Array<string>
}

// 系统状态

export type SystemStatus = {
    "uuid": string
}

// 测试结果
interface Detail {
    "name": string,
    "unit": string,
    "count": number,
    "run_time": {
        "name": string,
        "unit": string,
        "count": number,
        "mean": number,
        "min": number,
        "max": number,
        "25th_percentile": number,
        "50th_percentile": number,
        "75th_percentile": number,
        "90th_percentile": number,
        "95th_percentile": number,
        "99th_percentile": number,
        "99.9th_percentile": number,
        "std_dev": number
    }
}

export interface FinResult {
    "total_duration": number,
    "total_count": number,
    "query_on_time": number,
    "throughput": number,
    "all_metrics": Array<Detail>
}
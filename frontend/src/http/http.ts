const baseUrl = 'http://47.105.57.86:5000/'

// 定义接口以方便后续扩展和类型安全
interface RequestOptions {
  headers?: HeadersInit;
  body?: BodyInit | null;
}

class HttpClient {
  // 基础URL，可以是API服务器的地址
  private baseUrl: string;
  private defaultHeaders: HeadersInit;

  constructor(baseUrl: string, defaultHeaders?: HeadersInit) {
    this.baseUrl = baseUrl;
    this.defaultHeaders = defaultHeaders || {
      'Content-Type': 'application/json',  // 默认使用JSON作为请求体格式
    };
  }

  // GET请求
  async get(endpoint: string, options?: RequestOptions): Promise<any> {
    return this.request(endpoint, { method: 'GET', ...options });
  }

  // POST请求
  async post(endpoint: string, options?: RequestOptions): Promise<any> {
    return this.request(endpoint, { method: 'POST', ...options });
  }

  // PUT请求
  async put(endpoint: string, options?: RequestOptions): Promise<any> {
    return this.request(endpoint, { method: 'PUT', ...options });
  }

  // 私有方法执行请求
  private async request(endpoint: string, options?: RequestOptions & { method: string }): Promise<any> {
    const headers = { ...this.defaultHeaders, ...options?.headers };
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: options?.method,
      headers: headers,
      body: options?.body,
    });

    // 检查响应状态
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // 假设服务器总是返回JSON格式的数据
    return response.json();
  }
}

// 创建HttpClient实例，此处您需要替换成您的API基础URL
const httpClient = new HttpClient(baseUrl);

// 导出实例
export { httpClient };

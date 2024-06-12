const baseUrl = 'http://47.105.57.86:5003/'

// 定义接口以方便后续扩展和类型安全
interface RequestOptions {
  headers?: HeadersInit;
  body?: BodyInit | null;
}

class HttpClient {
  private baseUrl: string;
  private defaultHeaders: HeadersInit;
  constructor(baseUrl: string, defaultHeaders?: HeadersInit) {
    this.baseUrl = baseUrl;
    this.defaultHeaders = defaultHeaders || {
      'Content-Type': 'application/json',
    };
  }
  async get(endpoint: string, options?: RequestOptions): Promise<any> {
    return this.request(endpoint, { method: 'GET', ...options });
  }
  async post(endpoint: string, options?: RequestOptions): Promise<any> {
    return this.request(endpoint, { method: 'POST', ...options });
  }
  async put(endpoint: string, options?: RequestOptions): Promise<any> {
    return this.request(endpoint, { method: 'PUT', ...options });
  }
  private async request(endpoint: string, options?: RequestOptions & { method: string }): Promise<any> {
    const headers = { ...this.defaultHeaders, ...options?.headers };
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: options?.method,
      headers: headers,
      body: options?.body,
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  }
}

const httpClient = new HttpClient(baseUrl);

export { httpClient };

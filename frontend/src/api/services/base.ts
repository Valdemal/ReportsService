import axios from "axios";

export abstract class Service {
  protected abstract baseUrl: string;

  protected static API = axios.create();
}

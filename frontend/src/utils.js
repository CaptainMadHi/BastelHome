import { capitalize, camelCase } from "voca";

export function pascalCase(str) {
  return capitalize(camelCase(str));
}

export function desnakify(str) {
  return str ? str.replaceAll("_", " ") : "";
}

async function apiGeneric(url, options) {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response.json();
}

export async function apiGetDeviceTypes() {
  return apiGeneric("/api/device_types");
}

export async function apiGetDevices() {
  return apiGeneric("/api/devices");
}

export async function apiCommand(deviceHash, command, jsonPayload) {
  const method = command === "get" ? "GET" : "PUT";
  const url = `/api/command/${deviceHash}/${command}`
  const options = {
    headers: {
      "Accept": "application/json",
      "Content-Type": 'application/json'
    },
    method,
    body: jsonPayload ? JSON.stringify(jsonPayload) : undefined
  };
  const response = await apiGeneric(url, options);
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response.json();
}
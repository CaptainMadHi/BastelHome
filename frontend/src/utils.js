import { capitalize, camelCase, replaceAll } from "voca";

function dec2hex (dec) {
  return dec < 10
    ? '0' + String(dec)
    : dec.toString(16)
}

// generateId :: Integer -> String
export function generateCacheBuster (len=10) {
  var arr = new Uint8Array((len || 40) / 2);
  window.crypto.getRandomValues(arr);
  return Array.from(arr, dec2hex).join('');
}


export function pascalCase(str) {
  return capitalize(camelCase(str));
}

export function desnakify(str) {
  return replaceAll(str, "_", " ");
}

export function deepIncludes(arr, obj) {
  return arr.findIndex(x => JSON.stringify(x) === JSON.stringify(obj)) !== -1;
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
  const method = command === "get" ? "GET" : "POST";
  const url = `/api/command/${deviceHash}/${command}`
  const options = {
    headers: {
      "Accept": "application/json",
      "Content-Type": 'application/json'
    },
    method,
    body: jsonPayload ? JSON.stringify(jsonPayload) : undefined
  };
  return apiGeneric(url, options);
}
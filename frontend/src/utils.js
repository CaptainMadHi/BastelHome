import {capitalize, camelCase} from "voca";

export function pascalCase(str) {
  return capitalize(camelCase(str));
}

export function desnakify(str) {
  return str ? str.replaceAll("_", " ") : "";
}

export async function apiQuery(deviceHash, command, jsonPayload) {
  const method = command === "get" ? "GET" : "PUT";
  const response = await fetch(`/api/${deviceHash}/${command}`, {
    headers: {
      "Accept": "application/json",
      "Content-Type": 'application/json'
    },
    method,
    body: jsonPayload ? JSON.stringify(jsonPayload) : undefined
  });
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response.json();
}
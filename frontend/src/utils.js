export function desnakify(str) {
  return str ? str.replaceAll("_", " ") : "";
}
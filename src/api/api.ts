
export async function fetchData() {
    const response = await fetch('http://localhost:3000/api/data');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}

export async function fetchRadarData() {
    const response = await fetch('http://localhost:3000/api/radar');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}

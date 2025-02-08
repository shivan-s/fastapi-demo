import type { PageServerLoad, Actions } from './$types';

const API_URL = new URL('http://localhost:8000/');

export const load: PageServerLoad = async ({ fetch }) => {
	const response = await fetch(new URL('/', API_URL));
	const result = response.json() as Promise<{ message: string }>;
	return {
		result
	};
};

export const actions: Actions = {
	default: async ({ fetch, request }) => {
		const fd = await request.formData();
		const a = String(fd.get('a')!);
		const b = String(fd.get('b')!);
		const r = new Request(new URL('/addition', API_URL), {
			method: 'POST',
			headers: { 'content-type': 'application/json' },
			body: JSON.stringify({ a: parseInt(a), b: parseInt(b) })
		});
		const response = await fetch(r);
		const result = (await response.json()) as { result: number };
		return { result: result.result };
	}
};

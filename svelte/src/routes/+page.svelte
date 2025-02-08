<script lang="ts">
	import type { PageProps } from './$types';
	import { enhance } from '$app/forms';

	let { data, form }: PageProps = $props();
</script>

<h1>Addition</h1>

{#await data.result}
	Loading...
{:then result}
	{result.message}
{/await}

<form
	method="POST"
	id="addition"
	use:enhance={() => {
		return async ({ update }) => {
			await update({ reset: false });
		};
	}}
>
	<label>a:<input name="a" /></label>
	<span>+</span>
	<label>b:<input name="b" /></label>
	{#if form?.result}
		<span>=</span>
		<strong>{form.result}</strong>
	{/if}
</form>
<button form="addition" type="submit">Submit</button>

<style>
	form {
		display: flex;
		flex-direction: row;
		gap: 1rem;
		padding: 2rem;
	}
</style>

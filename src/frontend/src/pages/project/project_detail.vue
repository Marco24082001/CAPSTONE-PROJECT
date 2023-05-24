<template>
	<div>
		<h1>project detail</h1>
	</div>
</template>

<script>
export default {
	name: "project-detail",
	mounted() {
		console.log(this.$route.params.id);
	}
}
</script>
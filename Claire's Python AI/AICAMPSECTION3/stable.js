import { toBase64, uploadFile } from "./ai_camp_day3.js";

async function query(data) {
	const response = await fetch(
		"https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
		{
			headers: {
				Authorization: "Bearer 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",
				"Content-Type": "application/json",
			},
			method: "POST",
			body: JSON.stringify(data),
		}
	);
	const result = await response.blob();
	return result;
}
query({"inputs": ""}).then(async(response) => {
	let base64 = await toBase64(response)
    let imageURL = await uploadFile(base64)
    console.log(imageURL)
});

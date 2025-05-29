const BASE_URL = "http://127.0.0.1:8000";

export const convertUnit = async ({ category, from_u, to_u, value }) => {
  const response = await fetch(`${BASE_URL}/convert`, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      category: category,
      from_unit: from_u,
      to_unit: to_u,
      value: parseFloat(value),
    }),
  });

  if (!response.ok)
    throw new Error(`Conversion failed with status ${response.status}`);

  const data = await response.json();
  return data.result;
};

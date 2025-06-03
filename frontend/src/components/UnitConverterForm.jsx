import React, { useState } from "react";
import { convertUnit } from "../services/api";
import "./UnitConverterForm.css";

const categories = {
  length: [
    "meter",
    "kilometer",
    "millimeter",
    "centimeter",
    "inch",
    "foot",
    "yard",
    "mile",
  ],
  weight: ["gram", "milligram", "kilogram", "ounce", "pound"],
  temperature: ["celsius", "fahrenheit", "kelvin"],
};

function UnitConverterForm() {
  const [category, setCategory] = useState("length");
  const [fromUnit, setFromUnit] = useState("");
  const [toUnit, setToUnit] = useState("");
  const [value, setValue] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState("");

  function selectCategory(cat) {
    setCategory(cat);
    setFromUnit("");
    setToUnit("");
  }

  const validateForm = () => {
    //Validate theres no empty fields
    if (fromUnit === "" || toUnit === "" || !value.trim()) {
      setError("Fill all fields");
      return false;
    }
    //Validate theres no negative values for length and weight
    if (category === "length" || category === "weight") {
      setError("Negative values does not allowed for length and weight");
      return value >= 0;
    }

    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (loading) return;
    if (!validateForm()) return;

    try {
      setLoading(true);
      const res = await convertUnit({
        category: category,
        from_u: fromUnit,
        to_u: toUnit,
        value: value,
      });
      setResult(`${res} ${toUnit}`);
      setError(null);
    } catch (err) {
      setError(err.message || "An unexpected error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="unit-converter-container">
      <h2>Unit Converter</h2>

      <div className="category-buttons">
        {Object.keys(categories).map((cat) => (
          <button
            key={cat}
            onClick={() => selectCategory(cat)}
            className={category === cat ? "selected" : ""}
          >
            {cat.charAt(0).toUpperCase() + cat.slice(1)}
          </button>
        ))}
      </div>
      {result ? (
        <div className="result-message">
          <p style={{ color: "black" }}>{result}</p>
          <button
            className="reset-btn"
            onClick={() => {
              setFromUnit("");
              setToUnit("");
              setValue("");
              setResult("");
            }}
          >
            Reset
          </button>
        </div>
      ) : (
        <>
          <div className="form-inputs">
            <label>
              From:
              <select
                value={fromUnit}
                onChange={(e) => setFromUnit(e.target.value)}
              >
                <option value="">-- Select --</option>
                {categories[category].map((unit) => (
                  <option key={unit} value={unit}>
                    {unit}
                  </option>
                ))}
              </select>
            </label>

            <label>
              To:
              <select
                value={toUnit}
                onChange={(e) => setToUnit(e.target.value)}
              >
                <option value="">-- Select --</option>
                {categories[category].map((unit) => (
                  <option key={unit} value={unit}>
                    {unit}
                  </option>
                ))}
              </select>
            </label>

            <label>
              Value:
              <input
                type="number"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                placeholder="Enter value"
              />
            </label>
            {error && <div style={{color:"black"}}>{error}</div>}
          </div>
          <div className="button-container">
            <button className="calculate-button" onClick={handleSubmit}>
              Calculate
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default UnitConverterForm;

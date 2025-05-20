import React, { useState } from "react";
import "./UnitConverterForm.css";

const categories = {
  length: ['meter', 'kilometer', 'millimeter', 'centimeter', 'inch', 'foot', 'yard', 'mile'],
  weight: ['gram', 'milligram', 'kilogram', 'ounce', 'pound'],
  temperature: ['celsius', 'fahrenheit', 'kelvin'],
};

function UnitConverterForm() {
  const [category, setCategory] = useState("length");
  const [fromUnit, setFromUnit] = useState("");
  const [toUnit, setToUnit] = useState("");
  const [value, setValue] = useState("");

  function selectCategory(cat) {
    setCategory(cat);
    setFromUnit("");
    setToUnit("");
  }

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

      <div className="form-inputs">
        <label>
          From:
          <select value={fromUnit} onChange={(e) => setFromUnit(e.target.value)}>
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
          <select value={toUnit} onChange={(e) => setToUnit(e.target.value)}>
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
      </div>

      <div className="button-container">
        <button className="calculate-button">
        Calculate
        </button>
      </div>
    </div>
  );
}

export default UnitConverterForm;

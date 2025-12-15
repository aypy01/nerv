/**
 * NERV Custom Dropdown Logic + Clear Form
 * Clean + Correct Version (Option A)
 */

document.addEventListener("DOMContentLoaded", () => {

    // ======================
    // DROPDOWN LOGIC
    // ======================

    function closeAllDropdowns(except = null) {
        document.querySelectorAll(".custom-select-container.open")
            .forEach(c => {
                if (c !== except) c.classList.remove("open");
            });
    }

    // Open dropdown
    document.querySelectorAll(".custom-select-trigger").forEach(trigger => {
        trigger.addEventListener("click", function (e) {
            e.stopPropagation();
            const container = this.closest(".custom-select-container");

            closeAllDropdowns(container);
            container.classList.toggle("open");
        });
    });

    // Select option
    document.querySelectorAll(".custom-option").forEach(option => {
        option.addEventListener("click", function (e) {
            e.stopPropagation();

            const container = this.closest(".custom-select-container");
            const trigger = container.querySelector(".custom-select-trigger");
            const hidden = container.nextElementSibling;

            hidden.value = this.dataset.value;
            trigger.childNodes[0].nodeValue = this.textContent.trim() + " ";

            container.querySelectorAll(".custom-option").forEach(o => o.classList.remove("selected"));
            this.classList.add("selected");

            container.classList.remove("open");
        });
    });

    // Click outside closes all dropdowns
    document.addEventListener("click", () => closeAllDropdowns());


    // ======================
    // CLEAR BUTTON LOGIC
    // ======================

    const clearBtn = document.getElementById("clearBtn");
    const form = document.getElementById("titanic-form");

    if (clearBtn && form) {
        clearBtn.addEventListener("click", () => {

            // Reset all form inputs
            form.reset();

            // Reset hidden fields
            const pclassHidden = document.getElementById("pclass-hidden");
            const sexHidden = document.getElementById("sex-hidden");

            if (pclassHidden) pclassHidden.value = "";
            if (sexHidden) sexHidden.value = "";

            // Reset dropdown labels
            const triggers = document.querySelectorAll(".custom-select-trigger");
            if (triggers.length >= 2) {
                triggers[0].childNodes[0].nodeValue = "Select Class ";
                triggers[1].childNodes[0].nodeValue = "Select Gender ";
            }

            // Remove selected states
            document.querySelectorAll(".custom-option").forEach(opt => opt.classList.remove("selected"));

            // Reload the page to restore Predict button
            window.location.href = window.location.pathname;
        });
    }

    console.log("NERV dropdown + clear logic loaded.");
});

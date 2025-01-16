let currentSelection = null;
let originalText = null;
let translationTooltip = document.getElementById('translation-tooltip');

// Helper function to position the tooltip
function positionTooltip(x, y) {
    const tooltip = document.getElementById('translation-tooltip');
    const tooltipWidth = tooltip.offsetWidth;
    const tooltipHeight = tooltip.offsetHeight;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    // Adjust position to keep tooltip within viewport
    let finalX = Math.min(x, windowWidth - tooltipWidth - 10);
    let finalY = Math.min(y, windowHeight - tooltipHeight - 10);
    finalX = Math.max(finalX, 10);
    finalY = Math.max(finalY, 10);

    tooltip.style.left = finalX + 'px';
    tooltip.style.top = finalY + 'px';
}

// Handle text selection
document.addEventListener('mouseup', function(e) {
    const selection = window.getSelection();
    const selectedText = selection.toString().trim();

    if (selectedText && selectedText.length > 0) {
        currentSelection = selection;
        originalText = selectedText;

        // Get selection coordinates
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        
        // Position tooltip below the selection
        positionTooltip(
            rect.left + window.scrollX,
            rect.bottom + window.scrollY + 5
        );
        
        translationTooltip.style.display = 'block';
    } else {
        hideTooltip();
    }
});

// Hide tooltip when clicking outside
document.addEventListener('mousedown', function(e) {
    if (!translationTooltip.contains(e.target)) {
        hideTooltip();
    }
});

function hideTooltip() {
    translationTooltip.style.display = 'none';
    currentSelection = null;
    originalText = null;
}

// Function to translate selected text
async function translateSelection() {
    if (!currentSelection || !originalText) return;

    const targetLang = document.getElementById('target-language').value;
    const range = currentSelection.getRangeAt(0);
    
    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: originalText,
                target_lang: targetLang
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Translation failed');
        }

        const data = await response.json();
        
        // Create a span for the translated text
        const translatedSpan = document.createElement('span');
        translatedSpan.textContent = data.translated_text;
        translatedSpan.className = 'translated';
        translatedSpan.title = 'Original: ' + originalText;

        // Replace the selected text with the translation
        range.deleteContents();
        range.insertNode(translatedSpan);

        // Hide the tooltip
        hideTooltip();

    } catch (error) {
        console.error('Translation error:', error);
        alert('Translation failed: ' + error.message);
    }
}

// Initialize tooltip element reference
document.addEventListener('DOMContentLoaded', function() {
    translationTooltip = document.getElementById('translation-tooltip');
}); 
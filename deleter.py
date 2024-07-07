async function deleteTwitterPosts() {
  let deleteCount = 0;

  while (true) {
    // Find and click on the caret menu item
    const caretMenuItem = document.querySelector('[data-testid="caret"]');
    if (caretMenuItem) {
      caretMenuItem.click();
    } else {
      console.error('Caret menu item not found.');
      break; // Exit the loop if caret menu item is not found
    }

    // Wait briefly for the delete options to appear (adjust timing as needed)
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Find and click on the menu item related to deletion
    const deleteMenuItem = document.querySelector('[role="menuitem"]');
    if (deleteMenuItem) {
      deleteMenuItem.click();

      // Wait briefly for the confirmation modal to appear (adjust timing as needed)
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Find and click on the confirmation button
      const confirmButton = document.querySelector('[data-testid="confirmationSheetConfirm"]');
      if (confirmButton) {
        confirmButton.click();
        console.log('Post deleted successfully.');
        deleteCount++;
      } else {
        console.error('Confirmation button not found.');
        break; // Exit the loop if confirmation button is not found
      }
    } else {
      console.error('Delete menu item not found.');
      break; // Exit the loop if delete menu item is not found
    }

    // Wait briefly before attempting to delete the next post (adjust timing as needed)
    await new Promise(resolve => setTimeout(resolve, 2000));
  }

  console.log(`Deleted ${deleteCount} posts.`);
}

// Call the function to start deleting Twitter posts
deleteTwitterPosts();

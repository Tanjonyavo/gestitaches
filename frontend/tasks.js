async function showTasks() {
  const message = document.querySelector("#tasks-message");
  const list = document.querySelector("#tasks");

  try {
    const response = await fetch("/api/tasks", { cache: "no-store" });
    if (!response.ok) throw new Error("La liste est indisponible.");

    const tasks = await response.json();
    for (const task of tasks) {
      const item = document.createElement("li");
      const title = document.createElement("strong");
      const details = document.createElement("p");
      const dueDate = task.due_date || "Sans échéance";
      const status = task.completed ? "Terminée" : "À faire";

      title.textContent = task.title;
      details.textContent = [task.description, dueDate, status].filter(Boolean).join(" · ");
      item.append(title, details);
      list.append(item);
    }
    message.textContent = tasks.length ? "" : "Aucune tâche pour le moment.";
  } catch {
    message.textContent = "Impossible de charger les tâches. Rechargez la page.";
  }
}

showTasks();

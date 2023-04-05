const { Client } = require("@notionhq/client");

const notion = new Client({ auth: process.env.NOTION_KEY });

(async () => {
  const databaseId = "fdcfad677110425286d871c95575334f";
  const response = await notion.pages.create({
    parent: { database_id: databaseId },
    properties: {
      Company: {
        title: [
          {
            text: {
              content: "Facebook",
            },
          },
        ],
      },
      Stage: {
        status: {
          name: "Applied",
        },
      },
      Position: {
        multi_select: [
          {
            name: "Frontend Developer",
          },
        ],
      },
    },
  });
  console.log(response);
  console.log("Success! Entry added.");
})();
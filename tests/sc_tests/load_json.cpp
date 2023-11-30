#include <filesystem>
#include <fstream>
#include <nlohmann/json.hpp>
#include <string>

using json = nlohmann::json;

int main(){
    int total_num_requests = 0;
    std::string prompt_file_path = "/datasets/flexflow/chatgpt.json";

    std::ifstream file_handle(prompt_file_path);
    // assert(file_handle.good() && "Prompt file does not exist.");
    json prompt_json = json::parse(file_handle,
                                    /*parser_callback_t */ nullptr,
                                    /*allow_exceptions */ true,
                                    /*ignore_comments */ true);

    std::vector<std::string> prompts;
    for (auto &prompt : prompt_json) {
        std::string text = prompt.get<std::string>();
        printf("Prompt[%d]: %s\n", total_num_requests, text.c_str());
        total_num_requests++;
        prompts.push_back(text);
        // tree_model.generate(text, 128 /*max_sequence_length*/);
    }
    return 0;
}

